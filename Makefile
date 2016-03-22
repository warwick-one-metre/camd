RPMBUILD = rpmbuild --define "_topdir %(pwd)/build" \
        --define "_builddir %{_topdir}" \
        --define "_rpmdir %{_topdir}" \
        --define "_srcrpmdir %{_topdir}" \
        --define "_sourcedir %(pwd)"

GIT_VERSION = $(shell git name-rev --name-only --tags --no-undefined HEAD 2>/dev/null || echo git-`git rev-parse --short HEAD`)
SERVER_VERSION=$(shell awk '/Version:/ { print $$2; }' camera-server.spec)

all:
	mkdir -p build
	awk '{sub("SOFTWARE_VERSION = .*$$","SOFTWARE_VERSION = \"$(SERVER_VERSION) ($(GIT_VERSION))\""); print $0}' camd > camd.tmp
	sed 's/{CAMERA}/blue/g' camera-client.spec > blue-camera-client.spec
	sed 's/{CAMERA}/blue/g' camera-server.spec > blue-camera-server.spec
	sed 's/{CAMERA}/blue/g' completion/cam > completion/blue
	sed 's/{CAMERA}/blue/g' camd.service > blued.service
	cp cam blue
	cp camd.tmp blued
	${RPMBUILD} -ba blue-camera-server.spec
	${RPMBUILD} -ba blue-camera-client.spec
	sed 's/{CAMERA}/red/g' camera-client.spec > red-camera-client.spec
	sed 's/{CAMERA}/red/g' camera-server.spec > red-camera-server.spec
	sed 's/{CAMERA}/red/g' completion/cam > completion/red
	sed 's/{CAMERA}/red/g' camd.service > redd.service
	sed "s/INSTRUMENT_ARM = 'BLUE'/INSTRUMENT_ARM = 'RED'/" cam > red
	sed "s/INSTRUMENT_ARM = 'BLUE'/INSTRUMENT_ARM = 'RED'/" camd.tmp > redd
	${RPMBUILD} -ba red-camera-server.spec
	${RPMBUILD} -ba red-camera-client.spec
	mv build/noarch/*.rpm .
	rm -rf build *-camera-*.spec *-camera-*.spec completion/red completion/blue red redd  redd.service blue blued blued.service camd.tmp

