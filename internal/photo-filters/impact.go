package phfilter

import (
	"log"
)

type ImpactFilter struct {
	init bool
}

func NewImpactFilter() *ImpactFilter {
	return &ImpactFilter{true}
}

func (f *ImpactFilter) Process() {
	log.Print("Proccess_moc... impact filter inited: ", f.init)
}
