package main

import (
	"image"
	"image/png"
	"log"
	"math/rand"
	"os"

	//"github.com/segmentio/kafka-go"

	"github.com/fogleman/gg"

	phfilter "github.com/minmaxxxed/polozhenie/internal/photo-filters"
)

type Filter interface {
	Process(phfilter.Request) (image.Image, error)
}

func KafkaMocFilterGet() string {
	if rand.Int()%2 == 0 {
		return "Blur"
	}
	return "Impact"
}

func SaveToPng(img image.Image, path string) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}

	defer file.Close()

	png.Encode(file, img)

	return nil
}

func main() {
	filterMap := make(map[string]Filter)

	log.Print("Initing filters")

	filterMap["Blur"] = phfilter.NewBlurFilter()
	filterMap["Impact"] = phfilter.NewImpactFilter()

	log.Print("Filters inited")

	img, err := gg.LoadImage("./data/john.jpg")
	if err != nil {
		log.Fatal("Error: ", err.Error())
	}

	req := phfilter.Request{Img: img, Text: "я еблан", FontPath: "./data/ofont.ru_Impact.ttf"}

	imgNew, err := filterMap["Impact"].Process(req)
	if err != nil {
		log.Fatal("Error: ", err.Error())
	}

	err = SaveToPng(imgNew, "./result/res.png")

	if err != nil {
		log.Fatal("Error: ", err.Error())
	}

	// for i := 0; i < 5; i++ {
	// 	filterName := KafkaMocFilterGet()
	// 	filterMap[filterName].Process()
	// }

	log.Print("Stopping")

}
