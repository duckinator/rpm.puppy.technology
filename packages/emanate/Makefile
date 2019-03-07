all:
	spectool -g emanate.spec
	fedpkg --release f29 local
	fedpkg --release f29 lint --rpmlintconf ../rpmlint.conf
	cp noarch/*.rpm ../../repo/fedora/29/x86_64/

clean:
	fedpkg clean
	rm -f *.rpm

.PHONY: all clean
