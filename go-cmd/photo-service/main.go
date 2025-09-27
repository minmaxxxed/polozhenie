package main

import (
	"log"
	"math/rand"

	//"github.com/segmentio/kafka-go"

	filters "github.com/minmaxxxed/polozhenie/internal/photo-filters"
)

type Filter interface {
	Process()
}

func KafkaMocFilterGet() string {
	if rand.Int()%2 == 0 {
		return "Blur"
	}
	return "Impact"
}

func main() {
	filterMap := make(map[string]Filter)

	log.Print("Initing filters")

	filterMap["Blur"] = filters.NewBlurFilter()
	filterMap["Impact"] = filters.NewImpactFilter()

	log.Print("Filters inited")

	for i := 0; i < 5; i++ {
		filterName := KafkaMocFilterGet()
		filterMap[filterName].Process()
	}

	log.Print("Stopping")

}
