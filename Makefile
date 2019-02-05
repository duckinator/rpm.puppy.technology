FEDORA_X86_64_DIR := repo/fedora/29/x86_64/

# http://yum.baseurl.org/wiki/RepoCreate.html

all:
	$(MAKE) pip_rpm PACKAGE=emanate
	#$(MAKE) gem_rpm PACKAGE=how_is

# Usage: make update-metadata REPODIR=<repo dir>
update-metadata:
	test -n "${REPODIR}"
	cd ${REPODIR} && createrepo --update .
	# TODO: Figure out GPG stuff?
	#gpg --detach-sign --armor repodata/repomd.xml <Paste>

# Usage: make pip_rpm PACKAGE=<pypi package name>
pip_rpm: dirs
	cd ${FEDORA_X86_64_DIR} && fpm -s python -t rpm ${PACKAGE}
	$(MAKE) update-metadata REPODIR=${FEDORA_X86_64_DIR}

# Usage: make gem_rpm PACKAGE=<rubygems package name>
gem_rpm: dirs
	cd ${FEDORA_X86_64_DIR} && fpm -s gem -t rpm ${PACKAGE}

dirs:
	mkdir -p ${FEDORA_X86_64_DIR}

clean:
	rm repo/fedora/*/*/*.rpm

.PHONY: all clean dirs pip_rpm
