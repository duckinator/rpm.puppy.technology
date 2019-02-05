FEDORA_X86_64_DIR := repo/fedora/29/x86_64/

# http://yum.baseurl.org/wiki/RepoCreate.html

all:
	$(MAKE) pip_rpm PACKAGE=emanate ARGS='--name emanate'
	#$(MAKE) gem_rpm PACKAGE=how_is

# Usage: make update-metadata REPODIR=<repo dir>
update-metadata:
	test -n "${REPODIR}"
	createrepo --update ${REPODIR}
	# TODO: Figure out GPG stuff?
	#gpg --detach-sign --armor repodata/repomd.xml

# Usage: make pip_rpm PACKAGE=<pypi package name>
pip_rpm: dirs
	cd ${FEDORA_X86_64_DIR} && fpm -s python -t rpm ${ARGS} ${PACKAGE}
	$(MAKE) update-metadata REPODIR=${FEDORA_X86_64_DIR}

# Usage: make gem_rpm PACKAGE=<rubygems package name>
gem_rpm: dirs
	cd ${FEDORA_X86_64_DIR} && fpm -s gem -t rpm ${PACKAGE}


repo-rpm:
	cp repo/puppy-technology.repo puppy-technology-rpm/files/etc/yum.repos.d/puppy-technology.repo
	cd puppy-technology-rpm && fedpkg --release f29 local
	cd puppy-technology-rpm && fedpkg --release f29 lint

dirs:
	mkdir -p ${FEDORA_X86_64_DIR}

clean:
	rm -f repo/fedora/*/*/*.rpm

.PHONY: all clean dirs pip_rpm
