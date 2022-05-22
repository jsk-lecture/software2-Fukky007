	.file	"3.c"
	.text
	.p2align 4,,15
	.globl	fact
	.type	fact, @function
fact:
.LFB0:
	.cfi_startproc
	cmpl	$1, %edi
	movl	$1, %eax
	je	.L4
	.p2align 4,,10
	.p2align 3
.L3:
	imull	%edi, %eax
	subl	$1, %edi
	cmpl	$1, %edi
	jne	.L3
	rep ret
	.p2align 4,,10
	.p2align 3
.L4:
	rep ret
	.cfi_endproc
.LFE0:
	.size	fact, .-fact
	.section	.text.startup,"ax",@progbits
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB1:
	.cfi_startproc
	xorl	%eax, %eax
	ret
	.cfi_endproc
.LFE1:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
