# # use this if blender executable is in your PATH
blender := blender

# # use this if you have blender installed via flatpak
# blender := flatpak run org.blender.Blender

# # use this if you have a portable blender installation
# blender := ./blender-4.3.2-linux-x64/blender

current_dir := $(realpath .)

all: repository/*.zip repository/index.json

repository/*.zip: ./*/output/*.zip
	mkdir -p repository
	cp $^ repository

repository/index.json: ./repository/*.zip
	$(blender) --command extension server-generate --repo-dir=$(current_dir)/repository

clean:
	rm -rf repository/*
