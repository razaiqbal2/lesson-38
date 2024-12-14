name="Raza"
age=12
weight=63.2
student=True

#before datatyping
print("Datatyping of ",name," before datatyping  ",type(name))
print("Datatyping of ",age," before datatyping  ",type(age))
print("Datatyping of ",weight," before datatyping  ",type(weight))
print("Datatyping of ",student," before datatyping  ",type(student))

#after datatyping

age=str(age)
weight=str(weight)
student=float(student)
print("Datatyping of ",age," after datatyping  ",type(age))
print("Datatyping of ",weight," after datatyping  ",type(weight))
print("Datatyping of ",student," after datatyping  ",type(student))