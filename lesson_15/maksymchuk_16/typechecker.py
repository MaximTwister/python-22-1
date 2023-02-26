import ast
import inspect
import textwrap


def typechecker(f):
    def wrapper(*args, **kwargs):
        method_name: str = f.__name__
        _self = args[0]
        _class = _self.__class__
        # TODO: Iterate through (RegularClass, AbstractClass, AnotherRegularClass) and determine which class is Abstract.
        # TODO: If AbstractClasses > 1: Iterate through them and determine whom belong method: `method_name`
        parent_abstract_class = _class.__bases__[0]  # (AbstractClass,)

        child_annotations = f.__annotations__
        del child_annotations["return"]
        parent_annotations = getattr(parent_abstract_class, method_name).__annotations__
        parent_return_type = parent_annotations.pop("return")
        child_return_type = get_func_return_type(f)

        print(f"child `{method_name}` annotations: {child_annotations}")
        print(f"parent `{method_name}` annotations: {parent_annotations}")

        if child_return_type != parent_return_type:
            raise ValueError(
                f"Implemented abstract method `{method_name}` must return type {parent_return_type}"
            )

        # TODO: If annotation return types equal check
        # if ...

        # If annotation param types equal check
        if tuple(child_annotations.values()) != tuple(parent_annotations.values()):
            raise ValueError(
                f"Implemented abstract method `{method_name}` "
                f"must takes types: {tuple(parent_annotations.values())}"
            )

        # we always have `self` as first arg
        if len(args) > 1:
            args_types = [type(arg) for arg in args[1:]]
            if tuple(args_types) != tuple(parent_annotations.values()):
                raise ValueError(
                    f"Implemented abstract method `{method_name}` "
                    f"must takes *args, **kwargs with types: {tuple(parent_annotations.values())}"
                )

        return f(*args, **kwargs)
    return wrapper


def get_func_return_type(f):
    f_source: str = textwrap.dedent(inspect.getsource(f))
    print(f"func source:\n{f_source}")
    tree = ast.parse(f_source)
    for node in ast.walk(tree):
        if isinstance(node, ast.Return):
            return_expr = node.value
            return_expr_ast = ast.Expression(return_expr)
            return_expr_compiled = compile(return_expr_ast, "", "eval")
            return_value = eval(return_expr_compiled)
            return_type = type(return_value)
            print(f"`{f.__name__}` return value: {return_value}")
            print(f"`{f.__name__}` return type: {return_type}")
            return return_type
