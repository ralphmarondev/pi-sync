namespace PiSync.Room.Delete
{
    partial class RoomDeleteForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            btnDelete = new Button();
            lblTenantCount = new Label();
            label8 = new Label();
            lblRoomStatus = new Label();
            label6 = new Label();
            lblDoorStatus = new Label();
            label4 = new Label();
            lblRoomName = new Label();
            label2 = new Label();
            panel1.SuspendLayout();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = SystemColors.ButtonHighlight;
            panel1.Controls.Add(btnDelete);
            panel1.Controls.Add(lblTenantCount);
            panel1.Controls.Add(label8);
            panel1.Controls.Add(lblRoomStatus);
            panel1.Controls.Add(label6);
            panel1.Controls.Add(lblDoorStatus);
            panel1.Controls.Add(label4);
            panel1.Controls.Add(lblRoomName);
            panel1.Controls.Add(label2);
            panel1.Location = new Point(38, 30);
            panel1.Name = "panel1";
            panel1.Size = new Size(359, 404);
            panel1.TabIndex = 4;
            // 
            // btnDelete
            // 
            btnDelete.BackColor = Color.FromArgb(255, 192, 192);
            btnDelete.Cursor = Cursors.Hand;
            btnDelete.FlatAppearance.BorderSize = 0;
            btnDelete.FlatStyle = FlatStyle.Flat;
            btnDelete.Font = new Font("Courier New", 14F);
            btnDelete.Location = new Point(28, 337);
            btnDelete.Margin = new Padding(0);
            btnDelete.Name = "btnDelete";
            btnDelete.Size = new Size(306, 43);
            btnDelete.TabIndex = 8;
            btnDelete.Text = "DELETE";
            btnDelete.UseVisualStyleBackColor = false;
            btnDelete.Click += btnDelete_Click;
            // 
            // lblTenantCount
            // 
            lblTenantCount.AutoSize = true;
            lblTenantCount.Font = new Font("Courier New", 14F);
            lblTenantCount.Location = new Point(44, 274);
            lblTenantCount.Name = "lblTenantCount";
            lblTenantCount.Size = new Size(26, 27);
            lblTenantCount.TabIndex = 7;
            lblTenantCount.Text = "2";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Location = new Point(28, 243);
            label8.Name = "label8";
            label8.Size = new Size(166, 22);
            label8.TabIndex = 6;
            label8.Text = "Tenant Count:";
            // 
            // lblRoomStatus
            // 
            lblRoomStatus.AutoSize = true;
            lblRoomStatus.Font = new Font("Courier New", 14F);
            lblRoomStatus.Location = new Point(44, 198);
            lblRoomStatus.Name = "lblRoomStatus";
            lblRoomStatus.Size = new Size(96, 27);
            lblRoomStatus.TabIndex = 5;
            lblRoomStatus.Text = "Active";
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Location = new Point(28, 167);
            label6.Name = "label6";
            label6.Size = new Size(154, 22);
            label6.TabIndex = 4;
            label6.Text = "Room Status:";
            // 
            // lblDoorStatus
            // 
            lblDoorStatus.AutoSize = true;
            lblDoorStatus.Font = new Font("Courier New", 14F);
            lblDoorStatus.Location = new Point(44, 123);
            lblDoorStatus.Name = "lblDoorStatus";
            lblDoorStatus.Size = new Size(68, 27);
            lblDoorStatus.TabIndex = 3;
            lblDoorStatus.Text = "Open";
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(28, 92);
            label4.Name = "label4";
            label4.Size = new Size(154, 22);
            label4.TabIndex = 2;
            label4.Text = "Door Status:";
            // 
            // lblRoomName
            // 
            lblRoomName.AutoSize = true;
            lblRoomName.Font = new Font("Courier New", 14F);
            lblRoomName.Location = new Point(44, 48);
            lblRoomName.Name = "lblRoomName";
            lblRoomName.Size = new Size(54, 27);
            lblRoomName.TabIndex = 1;
            lblRoomName.Text = "A14";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(28, 17);
            label2.Name = "label2";
            label2.Size = new Size(70, 22);
            label2.TabIndex = 0;
            label2.Text = "Name:";
            // 
            // RoomDeleteForm
            // 
            AutoScaleDimensions = new SizeF(12F, 22F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(763, 527);
            Controls.Add(panel1);
            Font = new Font("Courier New", 12F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(4, 3, 4, 3);
            Name = "RoomDeleteForm";
            StartPosition = FormStartPosition.CenterParent;
            Text = "RoomDeleteForm";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel1;
        private Label lblTenantCount;
        private Label label8;
        private Label lblRoomStatus;
        private Label label6;
        private Label lblDoorStatus;
        private Label label4;
        private Label lblRoomName;
        private Label label2;
        private Button btnDelete;
    }
}