obj-m += kmod.o chardd.o ioctl_ex.o

KDIR := /lib/modules/$(shell uname -r)/build
PWD := $(shell pwd)

default:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) modules
	gcc -o ioctl_user ioctl_user.c

clean:
	$(MAKE) -C $(KDIR) SUBDIRS=$(PWD) clean 
	rm ioctl_user

