#include "pebble_process_info.h"
#include "src/resource_ids.auto.h"

const PebbleProcessInfo __pbl_app_info __attribute__ ((section (".pbl_header"))) = {
  .header = "PBLAPP",
  .struct_version = { PROCESS_INFO_CURRENT_STRUCT_VERSION_MAJOR, PROCESS_INFO_CURRENT_STRUCT_VERSION_MINOR },
  .sdk_version = { PROCESS_INFO_CURRENT_SDK_VERSION_MAJOR, PROCESS_INFO_CURRENT_SDK_VERSION_MINOR },
  .process_version = { 1, 0 },
  .load_size = 0xb6b6,
  .offset = 0xb6b6b6b6,
  .crc = 0xb6b6b6b6,
  .name = "wf_analog",
  .company = "MakeAwesomeHappen",
  .icon_resource_id = DEFAULT_MENU_ICON,
  .sym_table_addr = 0xA7A7A7A7,
  .flags = PROCESS_INFO_WATCH_FACE | PROCESS_INFO_ROCKY_APP | PROCESS_INFO_PLATFORM_EMERY,
  .num_reloc_entries = 0xdeadcafe,
  .uuid = { 0x5C, 0xBA, 0x27, 0xAA, 0x01, 0xDC, 0x40, 0x6A, 0xB2, 0x2C, 0x7E, 0xB2, 0x94, 0x4A, 0xB0, 0x33 },
  .virtual_size = 0xb6b6
};
