#!/usr/bin/env python

"""
 * CVE-2023-29489
 * CVE-2023-29489 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""


def writedata(output, data):
    with open(output, 'a') as file:
        file.write(data)
