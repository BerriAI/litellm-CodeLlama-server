import time, random, traceback
from copy import deepcopy
from litellm import completion

################ ERROR HANDLING #####################
# implement model fallbacks, cooldowns, and retries
# if a model fails assume it was rate limited and let it cooldown for 60s
def handle_error(data):
    import time
    # retry completion() request with fallback models
    response = None
    start_time = time.time()
    rate_limited_models = set()
    model_expiration_times = {}
    fallback_strategy=['gpt-4', 'claude-2']
    while response == None and time.time() - start_time < 45: # retry for 45s
      for model in fallback_strategy:
        try:
            if model in rate_limited_models: # check if model is currently cooling down
              if model_expiration_times.get(model) and time.time() >= model_expiration_times[model]:
                  rate_limited_models.remove(model) # check if it's been 60s of cool down and remove model
              else:
                  continue # skip model
            print(f"calling model {model}")
            response = completion(**data)
            if response != None:
              return response
        except Exception as e:
          rate_limited_models.add(model)
          model_expiration_times[model] = time.time() + 60 # cool down this selected model
          pass
    return response
    