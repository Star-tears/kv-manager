// This file is auto-generated by @hey-api/openapi-ts

export type Body_kv_upload_file = {
    file: (Blob | File);
};

export type HTTPValidationError = {
    detail?: Array<ValidationError>;
};

export type KvIdItem = {
    kvId: number;
};

export type KvItem = {
    key: string;
    langKey: string;
    value: string;
    langValue: string;
    kvId?: number | null;
};

export type KvRecordItem = {
    langValue: string;
    kvId: number;
};

export type LangKv = {
    langKey: string;
    langValue: string;
};

export type LangWithPath = {
    lang: string;
    path: string;
};

export type LanguageItemBase = {
    lang: string;
};

export type ResponseBase = {
    type?: string | null;
    code?: number;
    data: unknown;
};

export type ValidationError = {
    loc: Array<(string | number)>;
    msg: string;
    type: string;
};

export type $OpenApiTs = {
    '/api/v1/kv/create_lang': {
        post: {
            req: {
                requestBody: LanguageItemBase;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/get_lang_list': {
        get: {
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
            };
        };
    };
    '/api/v1/kv/update_kv': {
        post: {
            req: {
                requestBody: KvItem;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/get_kv_data': {
        post: {
            req: {
                requestBody: LangKv;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/get_kv_record': {
        post: {
            req: {
                requestBody: KvRecordItem;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/delete_kv': {
        post: {
            req: {
                requestBody: KvIdItem;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/get_all_null_value_kv': {
        post: {
            req: {
                requestBody: LanguageItemBase;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/upload_new_lang': {
        post: {
            req: {
                requestBody: LangWithPath;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/gen_ts': {
        post: {
            req: {
                requestBody: LanguageItemBase;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/merge_check': {
        post: {
            req: {
                requestBody: LangWithPath;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/upload-file': {
        post: {
            req: {
                formData: Body_kv_upload_file;
            };
            res: {
                /**
                 * Successful Response
                 */
                200: unknown;
                /**
                 * Validation Error
                 */
                422: HTTPValidationError;
            };
        };
    };
    '/api/v1/kv/download-file': {
        get: {
            res: {
                /**
                 * Successful Response
                 */
                200: unknown;
            };
        };
    };
    '/api/v1/common/get_version': {
        get: {
            res: {
                /**
                 * Successful Response
                 */
                200: ResponseBase;
            };
        };
    };
    '/': {
        get: {
            res: {
                /**
                 * Successful Response
                 */
                200: string;
            };
        };
    };
};