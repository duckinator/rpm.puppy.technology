all:
	spectool -g solvespace.spec
	fedpkg --release f29 local
	fedpkg --release f29 lint
	cp x86_64/*.rpm ../../repo/fedora/29/x86_64/

clean:
	fedpkg clean
	rm -f *.rpm

.PHONY: all clean
