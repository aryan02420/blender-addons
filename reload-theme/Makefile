# # use this if blender executable is in your PATH
blender := blender

# # use this if you have blender installed via flatpak
# blender := flatpak run org.blender.Blender

# # use this if you have a portable blender installation
# blender := ./blender-4.3.2-linux-x64/blender

current_dir := $(realpath .)

all: output/reload-theme.zip output/icon.png

output/reload-theme.zip: ./src/
	mkdir -p output
	@echo -e "\033[1;34mMAKE:\033[0m Validating extension..."
	$(blender) --command extension validate $(current_dir)/$^
	@echo -e "\033[1;34mMAKE:\033[0m Building extension..."
	$(blender) --command extension build --source-dir $(current_dir)/$^ --output-filepath $(current_dir)/$@

output/icon.png: ./assets/icon.svg
	mkdir -p output
	@echo -e "\033[1;34mMAKE:\033[0m Generating icon..."
	magick -density 960 $^ -resize 256x256 ./$@

clean:
	rm -rf output/*
