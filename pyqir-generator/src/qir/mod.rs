// Copyright (c) Microsoft Corporation.
// Licensed under the MIT License.

use inkwell::{attributes::AttributeLoc, module::Module, values::FunctionValue};

pub mod instructions;

pub(crate) fn create_entrypoint_function<'ctx>(
    context: &'ctx inkwell::context::Context,
    module: &Module<'ctx>,
) -> Result<FunctionValue<'ctx>, String> {
    let ns = "QuantumApplication";
    let method = "Run";
    let entrypoint_name = format!("{}__{}__body", ns, method);

    let void_type = context.void_type();
    let fn_type = void_type.fn_type(&[], false);
    let fn_value = module.add_function(entrypoint_name.as_str(), fn_type, None);

    let entrypoint_attribute = context.create_string_attribute("EntryPoint", "");
    fn_value.add_attribute(AttributeLoc::Function, entrypoint_attribute);

    let entrypoint = module
        .get_function(&entrypoint_name)
        .ok_or("Could not create entrypoint.")?;

    Ok(entrypoint)
}

#[cfg(test)]
mod tests {
    use super::*;
    use inkwell::context::Context;
    use qirlib::{codegen::CodeGenerator, module, passes::run_basic_passes_on};

    #[test]
    fn entrypoint_function_has_correct_signature_and_default_attribute() {
        let context = Context::create();
        let module = module::load_template("test", &context).unwrap();
        let generator = CodeGenerator::new(&context, module).unwrap();

        let entrypoint = create_entrypoint_function(generator.context, &generator.module).unwrap();
        let entry = generator.context.append_basic_block(entrypoint, "entry");
        generator.builder.position_at_end(entry);
        generator.builder.build_return(None);
        run_basic_passes_on(&generator.module);
        let ir_string = generator.get_ir_string();
        let expected = "; ModuleID = 'test'\nsource_filename = \"./module.ll\"\n\ndefine void @QuantumApplication__Run__body() #0 {\nentry:\n  ret void\n}\n\nattributes #0 = { \"EntryPoint\" }\n";
        assert_eq!(expected, ir_string);
    }
}
