import pandas as pd
import xgboost as xgb
import joblib
from resources import recommender


def data_load_chalets_recomendador():
	df = pd.read_excel('resources/recomendador_data/chaletsRecomen.xlsx')
	return df

def data_load_flats_recomendador():
	df = pd.read_excel('resources/recomendador_data/flatsRecomen.xlsx')
	return df

def data_load_flats():
	df = pd.read_csv('resources/reporting_datasets/flats_final_reporting_data.csv', sep = ';')
	return df

def data_load_chalets():
	df = pd.read_csv('resources/reporting_datasets/chalets_final_reporting_data.csv', sep = ';')
	return df

def data_load_images_chalets():
	df = pd.read_csv('resources/image_gallery_datasets/gallery_data.csv', sep=',')
	return df

def data_load_flats_predictions():
	df = pd.read_csv('resources/models_results_data/flats_results.csv',sep=',')
	return df

def data_load_chalets_predictions():
	df = pd.read_csv('resources/models_results_data/chalets_results.csv',sep=',')
	return df

def data_load_users_validated():
	df = pd.read_csv('resources/users_data/users_validated_data.csv',sep=',')
	return df

def model_flats_XGBM_Binary_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Flats_Binary.model')
	return model.predict(input_data)

def model_flats_XGBM_bigger_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Flats_Bigger.model')
	return model.predict(xgb.DMatrix(input_data))

def model_flats_XGBM_lower_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Flats_Lower.model')
	return model.predict(xgb.DMatrix(input_data))

def model_chalets_XGBM_Binary_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Chalets_Binary.model')
	return model.predict(input_data)

def model_chalets_XGBM_bigger_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Chalets_Bigger.model')
	return model.predict(input_data)

def model_chalets_XGBM_lower_predict(input_data):
	model = joblib.load('resources/models/model_XGBM_Chalets_Lower.model')
	return model.predict(input_data)

def model_chalets_RLogistic_interval(input_data):
	listaEntradaModeloAux,listaEntradaModelo = [], []
	listaEntradaModeloAux.append(input_data)
	listaEntradaModelo.append(listaEntradaModeloAux)
	model = joblib.load('resources/models/model_RL_Chalets_interval.model')
	return model.predict(listaEntradaModelo)

def model_flats_RLogistic_interval(input_data):
	listaEntradaModeloAux,listaEntradaModelo = [], []
	listaEntradaModeloAux.append(input_data)
	listaEntradaModelo.append(listaEntradaModeloAux)
	model = joblib.load('resources/models/model_RL_Flats_interval.model')
	return model.predict(listaEntradaModelo)

def recommender_get_recomendation(isChalet,bed,fbath,garage,zip_code,living_area,built_year,predicted_price):
	if isChalet == True:
		datosRecomendador = datosRecomendadorChalets = data_load_chalets_recomendador()
	else:
		datosRecomendador = data_load_flats_recomendador()
	
	recomendaciones = recommender.recom_correlation_st_lim(bed,fbath,garage,zip_code,living_area,built_year,predicted_price,datosRecomendador)
	return recomendaciones



