import pke
import openai
from nltk.tokenize import sent_tokenize
import replicate
from main import extract_pdf_file
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
    #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
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


def main():

    openai.api_key = "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"

    rt = extract_pdf_file("s12916-023-02774-1.pdf")

    #Extract Keywords from chunks
    keywords = tf_model(rt)
    print(keywords)





if __name__ == "__main__":
    main()

