package main

import "C"
import (
	"fmt"
	"os"
	"io"
	"gopkg.in/yaml.v2"
	"text/template"
	"io/ioutil"
)

type store struct{
	FileName string ;
	Values map[string]interface{};
}

func tpl(fileName string, vals interface{}, output string) error {
	tmpl, err := template.New(fileName).ParseFiles(fileName)
	if err != nil {
		return err
	}

	var file io.Writer
	if output != "" {
		f, _ :=os.Create(output)
		defer f.Close()
		file = f
	} else {
		file = os.Stdout
	}

	err = tmpl.Execute(file, vals)
	if err != nil {
		return err
	}
	return nil
}

func (s *store)getValues() {
    yamlFile, err := ioutil.ReadFile(s.FileName)
    if err != nil {
        fmt.Printf("yamlFile.Get err   #%v ", err)
	}
    err = yaml.Unmarshal(yamlFile, &s.Values)
    if err != nil {
		panic(err)
    }
}

//export RenderTemplate
func RenderTemplate(template, fileName, output string){
	s := store{FileName: fileName}
	s.getValues()
	err := tpl(template, s.Values, output)
	if err != nil {
		panic(err)
    }
}

func main(){
	// RenderTemplate("sample.tmpl", "values.yml", "")
}