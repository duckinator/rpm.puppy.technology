all:
	cp ../../repo/puppy-technology.repo files/etc/yum.repos.d/puppy-technology.repo
	fedpkg --release f29 local
	fedpkg --release f29 lint
	cp noarch/*.rpm ../../repo/repo.rpm

clean:
	fedpkg clean
	rm -f *.rpm

.PHONY: all clean
