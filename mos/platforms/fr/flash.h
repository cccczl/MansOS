/*
 * Copyright (c) 2012 the MansOS team. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *  * Redistributions of source code must retain the above copyright notice,
 *    this list of  conditions and the following disclaimer.
 *  * Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
 * OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * flash.h -- Internal flash memory constants
 */

#ifndef _PLATFORM_FLASH_H_
#define _PLATFORM_FLASH_H_

//
// On MSP430F573{6,7,8,9} 16kb internal flash memory is present
//
#define MSP430_FLASH_START 0xC200
#define MSP430_FLASH_END   0xFF80 // End of the flash memory: interrupt vector start
#define MSP430_FLASH_SIZE  (0xFFFF - MSP430_FLASH_START + 1)

//
// Flash segment size (this is the minimal flash area that can be erased)
//
#define MSP430_FLASH_SEGMENT_SIZE  512
//
// Flash block size (this is the maximal flash area that can be written at once)
//
#define MSP430_FLASH_BLOCK_SIZE    64 // XXX - ?

//
// Flash Information Memory range: 256 bytes in two 128-byte segments
//
#define MSP430_FLASH_INFOMEM_START 0x1800
#define MSP430_FLASH_INFOMEM_END   0x18FF
//
// Flash Information Memory segment size
//
#define MSP430_FLASH_INFOMEM_SEGMENT_SIZE  128

// TODO: BSL memory - from 0x1000 to 0x17FF in four 512 byte segments!

#endif
