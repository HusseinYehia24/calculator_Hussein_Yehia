from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")

name = "calculator_Hussein_Yehia"
version = "0.1"
default_task = "run_unit_tests"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Hussein_Yehia",
    )
    project.set_property("unittest_module_glob", "test_*")
