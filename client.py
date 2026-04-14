from openai import OpenAI
from config import get_settings
import re

api_key, model = get_settings()
client = OpenAI(api_key=api_key)
command="""[7:37 pm, 07/04/2026] Paras Sharma: Chat gpt pr dal jo a jae
[7:37 pm, 07/04/2026] Paras Sharma: Wahi
[7:37 pm, 07/04/2026] Paras Sharma: Name bhej de
[7:59 pm, 07/04/2026] Saurav MU: Dal de
[8:21 am, 13/04/2026] Saurav MU: Callage ara h n
[7:36 pm, 13/04/2026] Saurav MU: Manoj sir jo pdf send ki dekha bo kis liy h meri samjh nhi ari
[7:45 pm, 13/04/2026] Paras Sharma: mere bhi nhi a rhi samjh me
[9:06 pm, 13/04/2026] Saurav MU: Kisi se puch kya h ye ya project report k liy h
[9:06 pm, 13/04/2026] Paras Sharma: KAL DEKH LENGE
[9:08 pm, 13/04/2026] Saurav MU: Project to bna hi nhi apna fir kya hoga
[9:08 pm, 13/04/2026] Paras Sharma: BAn jarga
[9:09 pm, 13/04/2026] Saurav MU: Kb bnega yar exam ane bale h
[9:09 pm, 13/04/2026] Paras Sharma: hm
[9:11 pm, 13/04/2026] Saurav MU: Kisi git hub id se search krke lele"""

try:
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role":"system","content":"you are paras. reply in natural hinglish. output only the message text. do not include date, time, sender name, prefixes, labels, or chat format."},
            {"role":"user","content":command}
        ]
    )
except Exception as e:
    raise RuntimeError(f"OpenAI request failed: {e}") from e

response = completion.choices[0].message.content or ""
response = re.sub(r"^\s*\[[^\]]+\]\s*[^:]{1,80}:\s*", "", response, flags=re.MULTILINE)
response = re.sub(r"^\s*[^:\n]{1,80}:\s*", "", response, flags=re.MULTILINE)
print(response.strip())
