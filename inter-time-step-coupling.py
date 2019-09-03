#! /usr/bin/env python

model0.initialize()
model1.initialize()

time = model0.get_current_time()
end_time = model0.get_end_time()

while time < end_time:
    
    has_converged = False
    while has_converged is False:

        state1 = model1.get_value("some_state_variable")
        model0.set_value("some_state_variable", state1)
        model0.solve()

        state0 = model0.get_value("boundary_flows")
        model1.set_value("boundary_flows", state0)
        model1.solve()

        has_converged = check_convergence(model0, model1, convergence_criteria)

    model1.update()
    model0.update()

    time = model0.get_current_time()
