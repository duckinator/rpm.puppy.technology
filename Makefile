FEDORA_X86_DIR := repo/fedora/29/x86_64/

all:
	$(MAKE) pip_rpm PACKAGE=emanate
	#$(MAKE) gem_rpm PACKAGE=how_is

pip_rpm: dirs
	cd ${FEDORA_X86_DIR} && fpm -s python -t rpm ${PACKAGE}

gem_rpm: dirs
	cd ${FEDORA_X86_DIR} && fpm -s gem -t rpm ${PACKAGE}

dirs:
	mkdir -p ${FEDORA_X86_DIR}

clean:
	rm repo/fedora/*/*/*.rpm

.PHONY: all clean dirs pip_rpm
