#
# Copyright (C) 2022 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

from aospdtgen.proprietary_files.section import Section, register_section

class DrmSection(Section):
	name = "DRM"
	interfaces = [
		"android.hardware.drm",
		"vendor.mediatek.hardware.keymanage",
	]
	apexes = [
		"com.google.android.widevine.nonupdatable",
	]
	libraries = [
		"liboemcrypto",
	]
	folders = [
		"lib/mediacas",
		"lib/mediadrm",
		"lib/mtkdrm",
		"lib64/mediacas",
		"lib64/mediadrm",
		"lib64/mtkdrm",
	]
	properties_prefixes = {
		"drm.service.enabled": True,
		"ro.netflix.bsp_rev": True,
	}

class DrmQseeSection(Section):
	name = "DRM (Qualcomm Secure Execution Environment)"
	interfaces = [
		"vendor.qti.hardware.qseecom",
	]
	binaries = [
		"qseecomd",
	]
	libraries = [
		"libQSEEComAPI",
	]

class DrmQteeSection(Section):
	name = "DRM (Qualcomm Trusted Execution Environment)"
	interfaces = [
		"vendor.qti.hardware.qteeconnector",
	]
	libraries = [
		"libGPQTEEC_vendor",
		"libGPTEE_vendor",
		"libQTEEConnector_vendor",
	]

class DrmFirmwareSection(Section):
	name = "DRM firmware"
	folders = [
		"etc/firmware/drm",
	]
	patterns = [
		"(.*/)?firmware/widevine\..*",
	]

register_section(DrmSection)
register_section(DrmQseeSection)
register_section(DrmQteeSection)
register_section(DrmFirmwareSection)
