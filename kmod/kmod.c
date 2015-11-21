#include <linux/module.h>
#include <linux/version.h>
#include <linux/kernel.h>

static int __init kmod_init(void)
{
    printk(KERN_INFO "kmod registered\n");
    return 0;
}

static void __exit kmod_exit(void)
{
    printk(KERN_INFO "kmod unregistered\n");
}

module_init(kmod_init);
module_exit(kmod_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Junyoung Heo <jyheo0@gmail.com>");
MODULE_DESCRIPTION("Kernel module example for class");

