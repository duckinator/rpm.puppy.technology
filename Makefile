FEDORA_X86_DIR := repo/fedora/29/x86_64/

# http://yum.baseurl.org/wiki/RepoCreate.html

all:
	$(MAKE) pip_rpm PACKAGE=emanate
	#$(MAKE) gem_rpm PACKAGE=how_is

update-metadata:
	createrepo --update repo/
	# TODO: Figure out GPG stuff?
	#gpg --detach-sign --armor repodata/repomd.xml <Paste>

pip_rpm: dirs
	cd ${FEDORA_X86_DIR} && fpm -s python -t rpm ${PACKAGE}

gem_rpm: dirs
	cd ${FEDORA_X86_DIR} && fpm -s gem -t rpm ${PACKAGE}

dirs:
	mkdir -p ${FEDORA_X86_DIR}

clean:
	rm repo/fedora/*/*/*.rpm

.PHONY: all clean dirs pip_rpm
