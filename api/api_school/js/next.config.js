module.exports = {
    async headers() {
        return [
            {
                source: '/:path*',
                headers: [
                    {key: 'Access-Control-Allow_Owrigin', value: '*'}
                ]
            }
        ]
    }
}