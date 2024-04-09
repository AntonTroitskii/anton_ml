# # Do a summary *after* freezing the features and changing the output classifier layer (uncomment for actual output)
from torchinfo import summary


def get_simple_summary(model, input_shape=(24, 3, 100, 100)):

    return summary(model,
                   # make sure this is "input_size", not "input_shape" (batch_size, color_channels, height, width)
                   input_size=input_shape,
                   verbose=0,
                   col_names=["input_size", "output_size",
                              "num_params", "trainable"],
                   col_width=20,
                   row_settings=["var_names"]
                   )
