from git import RemoteProgress

class CloneProgress(RemoteProgress):

  def update(self, op_code, cur_count, max_count=None, message=""):
    end = "\r"

    if op_code & RemoteProgress.END:
      end = "," + RemoteProgress.DONE_TOKEN + "\n"

    op_code = op_code & RemoteProgress.OP_MASK

    if op_code == RemoteProgress.COUNTING:
      print("counting objects: %d %s" % (cur_count, str(message)), end=end)
    elif op_code == RemoteProgress.COMPRESSING:
      print("compressing objects: %d%% (%d/%d) %s" % ((cur_count/max_count) * 100, cur_count, max_count, str(message)), end=end)
    elif op_code == RemoteProgress.WRITING:
      print("writing objects: %d%% (%d/%d) %s" % ((cur_count/max_count) * 100, cur_count, max_count, str(message)), end=end)
    elif op_code == RemoteProgress.RESOLVING:
      print("remote: resolving deltas: %d%% (%d/%d) %s" % ((cur_count/max_count) * 100, cur_count, max_count, str(message)), end=end)
