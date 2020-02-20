#!/bin/bash

registry_images_base_path=/Users/anand/Documents/datapipeline/devcon_2020/face_recognition
profile_dir="${registry_images_base_path}/blob_images"
# az storage blob download-batch -d $profile_dir -s telemetry-data-store --pattern "image_test/*" --connection-string "AccountName=devcon2020;AccountKey=8kKEH1to8/e55NdmKT5RIMMpMM47cznExv5fHRfr18fGeRtGPIztizv7w6jeeyTlJ8p63zOvYj8fEvayhSopNA==;EndpointSuffix=core.windows.net;DefaultEndpointsProtocol=https;"
az storage blob download-batch -d $profile_dir -s user --pattern "profile/*" --connection-string "AccountName=devcon2020;AccountKey=8kKEH1to8/e55NdmKT5RIMMpMM47cznExv5fHRfr18fGeRtGPIztizv7w6jeeyTlJ8p63zOvYj8fEvayhSopNA==;EndpointSuffix=core.windows.net;DefaultEndpointsProtocol=https;"
profile_img_transform_dir="${registry_images_base_path}/transformed_ids"
files_in_profile_dir=(${profile_dir}/profile/*)
files_in_profile_dir=($(find $profile_dir -type f -name "*.png" -exec basename {} .png ';'))
for profile_image_filename in ${files_in_profile_dir[*]}
do
	IFS='_' read -r profile_id profile_name <<< "${profile_image_filename}"
	echo "$profile_id"
	echo "$profile_name"
	#mkdir -p ${profile_img_transform_dir}/${profile_name}_${profile_id}
	mkdir -p ${profile_img_transform_dir}/${profile_id}
	cp ${profile_dir}/image_test/${profile_image_filename}.png ${profile_img_transform_dir}/${profile_id}/
done