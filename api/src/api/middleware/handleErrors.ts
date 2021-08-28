import Exception from "../../core/exceptions/Exception";

function handleErrors(err, req, res, next) {
  console.log(err);

  if (err instanceof Exception) {
    return res.status(err.getStatus()).json({
      success: false,
      data: {
        error: err.getError(),
      },
    });
  }

  return res.status(500).json({
    status: false,
    data: {
      error: "Internal Server Error",
    },
  });
}

export default handleErrors;
