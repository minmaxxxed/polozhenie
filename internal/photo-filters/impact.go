package phfilter

import (
	"image"
	"log"

	"github.com/fogleman/gg"
)

type ImpactFilter struct {
	init bool
}

func NewImpactFilter() *ImpactFilter {
	return &ImpactFilter{true}
}

func (f *ImpactFilter) Process(request Request) (image.Image, error) {
	dc := gg.NewContextForImage(request.Img)

	if err := dc.LoadFontFace(request.FontPath, 96); err != nil {
		log.Print("Error while loading font: ", err.Error())
		return request.Img, err
	}

	bounds := request.Img.Bounds()
	log.Print(bounds.Max.X, bounds.Max.Y)
	dc.SetRGB(1, 1, 1)
	dc.DrawStringAnchored(request.Text, float64(bounds.Max.X)/2, 4*float64(bounds.Max.Y)/5, 0.5, 0.5)

	log.Print("Proccess_moc... impact filter inited: ", f.init)

	return dc.Image(), nil
}
