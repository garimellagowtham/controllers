FILE(REMOVE_RECURSE
  "../msg_gen"
  "../src/controllers/msg"
  "../msg_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "../src/controllers/msg/__init__.py"
  "../src/controllers/msg/_ctrl_command.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
