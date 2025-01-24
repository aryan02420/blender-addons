# # use this if blender executable is in your PATH
blender := blender

# # use this if you have blender installed via flatpak
# blender := flatpak run org.blender.Blender

# # use this if you have a portable blender installation
# blender := ./blender-4.3.2-linux-x64/blender

current_dir := $(realpath .)

SUBPROJECT_DIRS := $(shell find ./*/ -type f -name 'Makefile' -exec dirname {} \;)

all: repository/index.json

./*/output/*.zip:
	for dir in $(SUBPROJECT_DIRS); do \
		$(MAKE) -C $$dir; \
	done

repository/*.zip: ./*/output/*.zip
	mkdir -p repository
	cp $^ repository

repository/index.json: ./repository/*.zip
	$(blender) --command extension server-generate --repo-dir=$(current_dir)/repository

clean:
	rm -rf repository/*

clean-all: clean
	for dir in $(SUBPROJECT_DIRS); do \
		$(MAKE) -C $$dir clean; \
	done
