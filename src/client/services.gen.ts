// This file is auto-generated by @hey-api/openapi-ts

import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';
import type { $OpenApiTs } from './types.gen';

export class KvService {
    /**
     * Get Kv Data
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvGetKvData(data: $OpenApiTs['/api/v1/kv/get_kv_data']['get']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/get_kv_data']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/kv/get_kv_data',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Get Kv Record
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvGetKvRecord(data: $OpenApiTs['/api/v1/kv/get_kv_record']['get']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/get_kv_record']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/kv/get_kv_record',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Update Kv
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvUpdateKv(data: $OpenApiTs['/api/v1/kv/update_kv']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/update_kv']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/update_kv',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Delete Kv
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvDeleteKv(data: $OpenApiTs['/api/v1/kv/delete_kv']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/delete_kv']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/delete_kv',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Get Bucket List
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvGetBucketList(): CancelablePromise<$OpenApiTs['/api/v1/kv/get_bucket_list']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/kv/get_bucket_list'
        });
    }
    
    /**
     * Create Bucket
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvCreateBucket(data: $OpenApiTs['/api/v1/kv/create_bucket']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/create_bucket']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/create_bucket',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Rename Bucket
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvRenameBucket(data: $OpenApiTs['/api/v1/kv/rename_bucket']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/rename_bucket']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/rename_bucket',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Delete Bucket
     * @param data The data for the request.
     * @param data.requestBody
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static kvDeleteBucket(data: $OpenApiTs['/api/v1/kv/delete_bucket']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/delete_bucket']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/delete_bucket',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Upload File
     * @param data The data for the request.
     * @param data.formData
     * @returns unknown Successful Response
     * @throws ApiError
     */
    public static kvUploadFile(data: $OpenApiTs['/api/v1/kv/upload-file']['post']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/upload-file']['post']['res'][200]> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/v1/kv/upload-file',
            formData: data.formData,
            mediaType: 'multipart/form-data',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
    /**
     * Download File
     * @param data The data for the request.
     * @param data.requestBody
     * @returns unknown Successful Response
     * @throws ApiError
     */
    public static kvDownloadFile(data: $OpenApiTs['/api/v1/kv/download-file']['get']['req']): CancelablePromise<$OpenApiTs['/api/v1/kv/download-file']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/kv/download-file',
            body: data.requestBody,
            mediaType: 'application/json',
            errors: {
                422: 'Validation Error'
            }
        });
    }
    
}

export class CommonService {
    /**
     * Get Kv Data
     * @returns ResponseBase Successful Response
     * @throws ApiError
     */
    public static commonGetKvData(): CancelablePromise<$OpenApiTs['/api/v1/common/get_version']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/v1/common/get_version'
        });
    }
    
}

export class IndexService {
    /**
     * Home
     * @returns string Successful Response
     * @throws ApiError
     */
    public static indexHome(): CancelablePromise<$OpenApiTs['/']['get']['res'][200]> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/'
        });
    }
    
}