AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'chalk'
BUILD_TYPE = 'rocky'
BUNDLE_BIN_DIR = 'chalk'
BUNDLE_NAME = 'wf_analog.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_CHALK', 'PBL_COLOR', 'PBL_ROUND', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=180', 'PBL_DISPLAY_HEIGHT=180', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['chalk']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = []
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}
MESSAGE_KEYS_DEFINITION = '/Users/ezequieldeluca/Documents/Development/Projects/Pebble/wf_analog/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/ezequieldeluca/Documents/Development/Projects/Pebble/wf_analog/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/ezequieldeluca/Documents/Development/Projects/Pebble/wf_analog/build/js/message_keys.json'
NODE = '/Users/ezequieldeluca/.nvm/versions/node/v7.9.0/bin/node'
NODE_PATH = '/Users/ezequieldeluca/Library/Application Support/Pebble SDK/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/Users/ezequieldeluca/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/ezequieldeluca/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/chalk'
PEBBLE_SDK_ROOT = '/Users/ezequieldeluca/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['chalk', 'color', 'round', 'mic', 'strap', 'strappower', 'compass', 'health', '180w', '180h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'chalk', 'BUNDLE_BIN_DIR': 'chalk', 'BUILD_DIR': 'chalk', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_CHALK', 'PBL_COLOR', 'PBL_ROUND', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=180', 'PBL_DISPLAY_HEIGHT=180']}
PLATFORM_NAME = 'chalk'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}, u'sdkVersion': u'3', u'projectType': u'rocky', u'uuid': u'5cba27aa-01dc-406a-b22c-7eb2944ab033', 'messageKeys': {'ControlKeyResetRequest': 1, 'ControlKeyUnsupportedError': 4, 'ControlKeyChunk': 3, 'ControlKeyResetComplete': 2}, 'companyName': u'MakeAwesomeHappen', u'enableMultiJS': True, u'watchapp': {u'watchface': True}, 'versionLabel': u'1.0', 'longName': u'wf_analog', u'displayName': u'wf_analog', 'shortName': u'wf_analog', u'main': {u'rockyjs': u'src/rocky/index.js', u'pkjs': u'src/pkjs/index.js'}, u'resources': {u'media': []}, 'name': u'wf_analog'}
REQUESTED_PLATFORMS = []
RESOURCES_JSON = []
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['emery', 'diorite', 'chalk', 'basalt']
TIMESTAMP = 1494560514
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/Users/ezequieldeluca/Library/Application Support/Pebble SDK/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
