# Submodules are imported on demand by their callers — keeping this `__init__`
# empty avoids a circular import where importing `py_astealth.core.base_types`
# would otherwise pull `core.api_specification` → `core.codec` →
# `py_astealth.stealth_types` (which is itself loading and triggered the
# `core.base_types` import in the first place).
