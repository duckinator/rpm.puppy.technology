all:
	spectool -g trufont.spec
	fedpkg --release f29 local
	#fedpkg --release f29 lint --rpmlintconf ../rpmlint.conf
	cp x86_64/*.rpm ../../repo/fedora/29/x86_64/

lint:
	@echo 'TODO: Resolve "missing-call-to-chdir-with-chroot" error.'
	fedpkg --release f29 lint --rpmlintconf ../rpmlint.conf

clean:
	fedpkg clean
	rm -f *.rpm

.PHONY: all clean
