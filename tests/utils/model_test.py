from typing import Optional, List, Union, Dict

from pydantic import BaseModel


# Define the PipeParams data class using Pydantic
class PipeParams(BaseModel):
    pipe_key: str
    param_setter: str
    param_val: Union[str, int, float, bool, Dict[str, str], Dict[str, List[str]]]


# Define the NluTest data class using Pydantic
class NluTest(BaseModel):
    nlu_ref: str
    lang: str
    test_group: str
    input_data_type: str
    library: str
    output_levels: Optional[List[str]] = None
    pipe_params: Optional[List[PipeParams]] = None


all_tests = [
    NluTest(nlu_ref="chunk", lang='en', test_group='chunker', input_data_type='generic', library='open_source'),
    NluTest(nlu_ref="ngram", lang='en', test_group='chunker', input_data_type='generic', library='open_source'),
    NluTest(nlu_ref="zh.segment_words", lang='zh', test_group='tokenizer', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="zh.tokenize", lang='zh', test_group='tokenizer', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="tokenize", lang='en', test_group='tokenizer', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.assert.biobert", lang='en', test_group='assertion', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="relation.drug_drug_interaction", lang='en', test_group='relation', input_data_type='medical',
            output_levels=['chunk', 'tokens', 'embeddings', 'document', 'relation'], library='healthcare'),
    NluTest(nlu_ref="pdf2table", lang='en', test_group='table_extractor', input_data_type='PPT_table',
            library='ocr'),
    NluTest(nlu_ref="ppt2table", lang='en', test_group='table_extractor', input_data_type='PDF_table',
            library='ocr'),
    NluTest(nlu_ref="doc2table", lang='en', test_group='table_extractor', input_data_type='DOC_table',
            library='ocr'),
    NluTest(nlu_ref="en.classify.albert.ag_news", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.albert.imdb", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.bert_sequence.dehatebert_mono", lang='en', test_group='classifier',
            input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.bert.zero_shot_classifier", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.speech2text.wav2vec2.v2_base_960h", lang='en', test_group='classifier',
            input_data_type='asr',
            library='open_source'),
    NluTest(nlu_ref="en.speech2text.hubert", lang='en', test_group='classifier', input_data_type='asr',
            library='open_source'),
    NluTest(nlu_ref="cyberbullying", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.news.deberta.small", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="e2e", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="emotion", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="pos", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.distilbert.zero_shot_classifier", lang='en', test_group='classifier',
            input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="tr.distilbert.zero_shot_classifier.allnli", lang='tr', test_group='classifier',
            input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="lang", lang='fr', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="lang", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="fr.classify.camembert.base", lang='fr', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.ag_news.longformer", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.imdb.longformer", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="zh.ner", lang='zh', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.ner.onto.glove.6B_100d", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="questions", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.roberta.zero_shot_classifier", lang='en', test_group='classifier',
            input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="sarcasm", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="sentiment.imdb", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="sentiment.twitter", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="sentiment.vivekn", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.roberta.imdb", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.snips", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="spam", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="toxic", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.ner.camembert", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.ag_news.xlnet", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify.imdb.xlnet", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="yake", lang='en', test_group='classifier', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.classify_image.base_patch16_224", lang='en', test_group='classifier',
            input_data_type='IMG_vit',
            library='open_source'),
    NluTest(nlu_ref="en.classify_image.swin.tiny", lang='en', test_group='classifier', input_data_type='IMG_vit',
            library='open_source'),
    NluTest(nlu_ref="en.answer_question.tapas.wikisql.base_finetuned", lang='en', test_group='classifier',
            input_data_type='tapas',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="embed_sentence.bert", lang='en', test_group='sentence_embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="embed_sentence.electra", lang='en', test_group='sentence_embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="bert", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="xx.embed.distilbert", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="bert electra", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="glove", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="bert en.embed.bert.small_L8_128  electra", lang='en', test_group='embedding',
            input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.embed.roberta", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="xx.embed.xlm", lang='en', test_group='embedding', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="norm_document", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="lemma", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="norm", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="xx.sentence_detector", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="stem", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="stopwords", lang='en', test_group='pre_processing', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.seq2seq.distilbart_cnn_6_6", lang='en', test_group='seq2seq', input_data_type='summarizer',
            library='open_source',
            pipe_params=[PipeParams(pipe_key='bart_transformer', param_setter='setTask', param_val='summarize:'),
                         PipeParams(pipe_key='bart_transformer', param_setter='setMaxOutputLength',
                                    param_val=200)]),
    NluTest(nlu_ref="xx.de.translate_to.en", lang='de', test_group='seq2seq', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.coreference.spanbert", lang='en', test_group='span_bert_coref', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="dep.typed", lang='en', test_group='typed_dependency', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="dep.untyped", lang='en', test_group='untyped_dependency', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.bert.base", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="fr.answer_question.camembert.fquad", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.deberta", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.distil_bert.base_cased", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.longformer.base", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.roberta.base.by_deepset", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="en.answer_question.squadv2.xlm_roberta.base", lang='en', test_group='span_classifier',
            input_data_type='qa',
            output_levels=['chunk', 'tokens', 'embeddings'], library='open_source'),
    NluTest(nlu_ref="ner.onto", lang='en', test_group='pipeline', input_data_type='generic', library='open_source'),
    NluTest(nlu_ref="en.t5.small", lang='en', test_group='seq2seq', input_data_type='generic',
            library='open_source',
            pipe_params=[PipeParams(pipe_key='t5_transformer', param_setter='setTask',
                                    param_val='translate English to French')]),
    NluTest(nlu_ref="match.chunks", lang='en', test_group='matcher', input_data_type='generic',
            library='open_source'),
    NluTest(nlu_ref="en.de_identify", lang='en', test_group='hc_deidentification', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.norm_drugs", lang='en', test_group='hc_drugnormalizer', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="bert elmo", lang='en', test_group='hc_genericclassifier', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.classify.ade.conversational", lang='en', test_group='hc_licensedclassifier',
            input_data_type='medical', library='healthcare'),
    NluTest(nlu_ref="en.med_ner.tumour en.med_ner.radiology en.med_ner.diseases en.ner.onto", lang='en',
            test_group='hc_pipeline', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.explain_doc.era", lang='en', test_group='hc_pipeline', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.med_ner.diseases en.resolve.icd10cm.augmented_billable", lang='en',
            test_group='hc_resolver',
            input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.summarize.clinical_jsl", lang='en', test_group='hc_summarizer', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.generate.generic_flan_base", lang='en', test_group='hc_generation',
            input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="en.zero_shot.ner_roberta", lang='en', test_group='hc_generation', input_data_type='medical',
            library='healthcare',
            output_levels=["sentence"],
            pipe_params=[PipeParams(pipe_key='zero_shot_ner', param_setter='setEntityDefinitions', param_val={
                "PROBLEM": [
                    "What is the disease?",
                    "What is his symptom?",
                    "What is her disease?",
                    "What is his disease?",
                    "What is the problem?",
                    "What does a patient suffer",
                    "What was the reason that the patient is admitted to the clinic?",
                ],
                "DRUG": [
                    "Which drug?",
                    "Which is the drug?",
                    "What is the drug?",
                    "Which drug does he use?",
                    "Which drug does she use?",
                    "Which drug do I use?",
                    "Which drug is prescribed for a symptom?",
                ],
                "ADMISSION_DATE": ["When did patient admitted to a clinic?"],
                "PATIENT_AGE": [
                    "How old is the patient?",
                    "What is the gae of the patient?",
                ],
            })]),
    NluTest(nlu_ref="en.med_ner.clinical en.relation.zeroshot_biobert", lang='en', test_group='hc_generation',
            input_data_type='medical', library='healthcare',
            pipe_params=[
                PipeParams(pipe_key='zero_shot_relation_extraction', param_setter='setRelationalCategories',
                           param_val={
                               "CURE": ["{{TREATMENT}} cures {{PROBLEM}}."],
                               "IMPROVE": ["{{TREATMENT}} improves {{PROBLEM}}.",
                                           "{{TREATMENT}} cures {{PROBLEM}}."],
                               "REVEAL": ["{{TEST}} reveals {{PROBLEM}}."]}),
                PipeParams(pipe_key='zero_shot_relation_extraction', param_setter='setMultiLabel',
                           param_val=False)]),
    NluTest(nlu_ref="en.classify_image.convnext.tiny", lang='en', test_group='img_classifier',
            input_data_type='IMG_classifier', library='ocr'),

]


one_per_lib = [
    NluTest(nlu_ref="chunk", lang='en', test_group='chunker', input_data_type='generic', library='open_source'),
    NluTest(nlu_ref="en.assert.biobert", lang='en', test_group='assertion', input_data_type='medical',
            library='healthcare'),
    NluTest(nlu_ref="ppt2table", lang='en', test_group='table_extractor', input_data_type='PDF_table',
            library='ocr'),
]