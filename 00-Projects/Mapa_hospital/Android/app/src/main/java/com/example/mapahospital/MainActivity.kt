package com.example.mapahospital

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.webkit.CookieManager
import android.webkit.WebChromeClient
import android.webkit.WebStorage
import android.webkit.WebView
import android.webkit.WebViewClient

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val myWebView: WebView = findViewById(R.id.webView)
        clearWebViewCache(myWebView)
        myWebView.loadUrl("https://mapahospital.ovh")
        myWebView.webChromeClient = WebChromeClient()

        val webSettings = myWebView.settings
        webSettings.javaScriptEnabled = true
        webSettings.loadWithOverviewMode = true
        webSettings.useWideViewPort = true

        myWebView.webViewClient = WebViewClient()

    }

    private fun clearWebViewCache(webView: WebView) {
        // Limpia el caché de la WebView
        webView.clearCache(true)

        // Limpia los datos de formularios
        webView.clearFormData()

        // Limpia el historial
        webView.clearHistory()

        // Limpia las cookies
        val cookieManager = CookieManager.getInstance()
        cookieManager.removeAllCookies(null)
        cookieManager.flush()

        // Limpia el almacenamiento local
        WebStorage.getInstance().deleteAllData()
    }
}

