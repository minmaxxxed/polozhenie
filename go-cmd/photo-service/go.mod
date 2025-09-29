module github.com/minmaxxxed/polozhenie/go-cmd/photo-service

go 1.24.1

require (
	github.com/fogleman/gg v1.3.0
	github.com/minmaxxxed/polozhenie/internal/photo-filters v0.0.0-20250929175300-4139e0c2ecdc
)

require (
	github.com/golang/freetype v0.0.0-20170609003504-e2365dfdc4a0 // indirect
	golang.org/x/image v0.31.0 // indirect
)

//replace github.com/minmaxxxed/polozhenie/internal/photo-filters => ../../internal/photo-filters
