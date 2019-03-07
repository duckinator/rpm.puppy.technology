FEDORA_X86_64_DIR := repo/fedora/29/x86_64/

# http://yum.baseurl.org/wiki/RepoCreate.html

all:
	@echo "Usage: make <PACKAGE NAME>"
	@echo
	@echo "Known packages: emanate, solvespace"

emanate:
	# NOTE: Remove `--iteration` once emanate >v5.0.0 is released.
	$(MAKE) pip_rpm PACKAGE=emanate ARGS='--name emanate --iteration 2'

solvespace:
	$(MAKE) package PACKAGE=solvespace

# Usage: make update-metadata REPODIR=<repo dir>
update-metadata:
	test -n "${REPODIR}"
	createrepo --update ${REPODIR}
	# TODO: Figure out GPG stuff?
	#gpg --detach-sign --armor repodata/repomd.xml

package: dirs
	$(MAKE) -C packages -C "${PACKAGE}"
	$(MAKE) update-metadata REPODIR=${FEDORA_X86_64_DIR}

# Usage: make pip_rpm PACKAGE=<pypi package name>
pip_rpm: dirs
	cd ${FEDORA_X86_64_DIR} && fpm -s python -t rpm --python-bin /usr/bin/python3 ${ARGS} ${PACKAGE}
	$(MAKE) update-metadata REPODIR=${FEDORA_X86_64_DIR}


repo-rpm:
	cp repo/puppy-technology.repo puppy-technology-rpm/files/etc/yum.repos.d/puppy-technology.repo
	cd puppy-technology-rpm && fedpkg --release f29 local
	cd puppy-technology-rpm && fedpkg --release f29 lint

dirs:
	mkdir -p ${FEDORA_X86_64_DIR}

.PHONY: all dirs pip_rpm
