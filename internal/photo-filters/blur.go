package phfilter

import (
	"log"
)

type BlurFilter struct {
	init bool
}

func NewBlurFilter() *BlurFilter {
	return &BlurFilter{true}
}

func (f *BlurFilter) Process() {
	log.Print("Proccess_moc... blur filter inited: ", f.init)
}
