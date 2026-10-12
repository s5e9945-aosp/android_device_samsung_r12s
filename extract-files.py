#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/samsung/s5e9945',
    'hardware/samsung_slsi-linaro/exynos',
    'hardware/samsung_slsi-linaro/graphics',
    'vendor/samsung/s5e9945',
]


blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/hw/camera.s5e9945.so': blob_fixup()
        .add_needed('libui_shim.so')
        .remove_needed('libcav.so')
        .remove_needed('vendor.samsung.hardware.thermal@1.0.so')
        .sig_replace('ba e2 01 94', '1f 20 03 d5')
        .sig_replace('70 e2 01 94', '1f 20 03 d5'),
}

module = ExtractUtilsModule(
    'r12s',
    'samsung',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 's5e9945', module.vendor)
    utils.run()
