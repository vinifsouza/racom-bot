class Exception extends Error {
  private status: number;
  private error: object;

  constructor(status = 500, error = null) {
    super(error);

    this.status = status;
    this.error = error;
  }

  public getStatus(): number {
    return this.status;
  }

  public getError(): object {
    return this.error;
  }
}

export default Exception;
