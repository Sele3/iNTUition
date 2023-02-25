import pke
import openai
from nltk.tokenize import sent_tokenize
import replicate
import os
#from main import extract_pdf_file
from urllib.request import urlretrieve
MAX_LENGTH = 1000

ABBR = {"cvd": "Cardiovascular disease", "t2dm": "Type 2 diabetes", "incident cvd": "Incident Cardiovascular disease"}


def return_top_keywords(keyphrase):
    ans = list(map(lambda x: x[0], keyphrase))
    for i in range(len(ans)):
        if ans[i] in ABBR.keys():
            ans[i] = ABBR[ans[i]]

    return ans


def split_into_chunks(rt):
    arr = []
    string = ""
    for s in sent_tokenize(rt):
        string += s
        if len(string) > MAX_LENGTH:
            arr.append(string)
            string = ""

    return arr


def summarise(para):
    #Rewrite this for brevity, in outline form
    #
    model_engine = "text-davinci-003"
    prompt = "Rewrite this for brevity, in outline form" + para

    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response


def tf_model(rt):
    #initialize model
    e = pke.unsupervised.TfIdf()

    e.load_document(input=rt, language='en')
    e.candidate_selection()                     # identify keyphrase candidates
    e.candidate_weighting()                     # weight keyphrase candidates
    keyphrases = e.get_n_best(n=5, stemming=False)

    # for each of the best candidates
    for i, (candidate, score) in enumerate(keyphrases):
        # print out the its rank, phrase and score
        print("rank {}: {} ({})".format(i, candidate, score))

    return return_top_keywords(keyphrases)


def infographic(key, filepath):
    #\frontend\public\media
    #
    os.environ["REPLICATE_API_TOKEN"] = ""
    model = replicate.models.get("stability-ai/stable-diffusion")
    version = model.versions.get("db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf")
    prompt = ",".join(['infographic', 'medical']+key)

    inputs = {
    # Input prompt
    'prompt': prompt,

    # pixel dimensions of output image
    'image_dimensions': "768x768",

    # Specify things to not see in the output
    # 'negative_prompt': ...,

    # Number of images to output.
    # Range: 1 to 4
    'num_outputs': 1,

    # Number of denoising steps
    # Range: 1 to 500
    'num_inference_steps': 50,

    # Scale for classifier-free guidance
    # Range: 1 to 20
    'guidance_scale': 7.5,

    # Choose a scheduler.
    'scheduler': "DPMSolverMultistep",

    # Random seed. Leave blank to randomize the seed
    # 'seed': ...,
    }

    print(prompt)
    link = version.predict(**inputs)
    urlretrieve(link[0], "./frontend/public/media/infographic.png")


def generate_infographic(text: str) -> None:
    keywords = tf_model(text)
    infographic(keywords, "./frontend/public/media/infographic.png")


# def main():
#     #extract file from filepath
#     rt = extract_pdf_file("s12916-023-02774-1.pdf")

#     #Extract Keywords from chunks
#     keywords = tf_model(rt)


#     infographic(keywords, "./frontend/public/media/infographic.png")


# if __name__ == "__main__":
#     main()

