package com.ralphmarondev.pisync.features.auth.presentation.components


import androidx.compose.foundation.Image
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.outlined.NetworkWifi
import androidx.compose.material3.Button
import androidx.compose.material3.ElevatedButton
import androidx.compose.material3.ElevatedCard
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.window.Dialog
import androidx.compose.ui.window.DialogProperties
import coil.compose.rememberAsyncImagePainter
import com.ralphmarondev.pisync.R

@Composable
fun SetupServerIpDialog(
    onDismiss: () -> Unit,
    onSave: (String) -> Unit
) {
    var serverIp by remember { mutableStateOf("") }

    Dialog(
        onDismissRequest = onDismiss,
        properties = DialogProperties(
            dismissOnClickOutside = false,
            dismissOnBackPress = false
        )
    ) {
        ElevatedCard(
            modifier = Modifier
                .fillMaxWidth()
                .padding(8.dp)
        ) {
            Column(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp),
                horizontalAlignment = Alignment.CenterHorizontally
            ) {
                Image(
                    painter = rememberAsyncImagePainter(R.drawable.ip_address),
                    contentDescription = null,
                    contentScale = ContentScale.Crop,
                    modifier = Modifier
                        .size(60.dp)
                )

                Spacer(modifier = Modifier.height(8.dp))
                Text(
                    text = "Setup Server",
                    fontSize = 14.sp,
                    color = MaterialTheme.colorScheme.secondary
                )

                Spacer(modifier = Modifier.height(16.dp))
                NormalTextField(
                    value = serverIp,
                    onValueChange = { serverIp = it },
                    placeholder = "192.68.0.0",
                    label = "Ip Address",
                    modifier = Modifier
                        .padding(horizontal = 16.dp, vertical = 4.dp),
                    leadingIcon = Icons.Outlined.NetworkWifi
                )

                Row(
                    modifier = Modifier
                        .fillMaxWidth(),
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(16.dp)
                ) {
                    Button(
                        onClick = {
                            if (serverIp.isNotEmpty()) {
                                onSave(serverIp)
                            }
                        },
                        modifier = Modifier.padding(16.dp)
                    ) {
                        Text(
                            text = " SAVE ",
                            fontSize = 16.sp,
                            fontWeight = FontWeight.W500
                        )
                    }

                    ElevatedButton(
                        onClick = onDismiss
                    ) {
                        Text(
                            text = "CANCEL",
                            fontSize = 16.sp,
                            fontWeight = FontWeight.W500
                        )
                    }
                }
            }
        }
    }
}